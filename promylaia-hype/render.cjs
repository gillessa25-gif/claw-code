// Rendu image par image de index.html via Chromium (Playwright) -> ffmpeg.
//   node render.cjs v,s,h                 -> out/promylaia-hype-<format>.mp4
//   node render.cjs v --stills 0,2.5,12.6  -> out/stills/<format>-<t>.png
const path = require("path");
const fs = require("fs");
const { spawn } = require("child_process");
let chromium;
try { ({ chromium } = require("playwright")); } catch { ({ chromium } = require("/opt/node-tools/node_modules/playwright")); }

const FPS = 30, DUR = 30;
const SIZES = { v: [1080, 1920, "9x16"], s: [1080, 1080, "1x1"], h: [1920, 1080, "16x9"] };
const fmts = (process.argv[2] || "v,s,h").split(",");
const si = process.argv.indexOf("--stills");
const stills = si > 0 ? process.argv[si + 1].split(",").map(Number) : null;
const root = __dirname;

async function renderFormat(browser, f) {
  const [w, h, tag] = SIZES[f];
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  page.on("pageerror", e => console.error(`[${f}] page error:`, e.message));
  await page.goto("file://" + path.join(root, "index.html") + "?fmt=" + f);
  await page.waitForFunction(() => window.READY === true, null, { timeout: 30000 });

  if (stills) {
    fs.mkdirSync(path.join(root, "out/stills"), { recursive: true });
    for (const t of stills) {
      await page.evaluate(t => window.render(t), t);
      await page.screenshot({ path: path.join(root, `out/stills/${f}-${t.toFixed(2)}.png`) });
    }
    return;
  }
  const out = path.join(root, `out/promylaia-hype-${tag}.mp4`);
  const ff = spawn("ffmpeg", ["-y", "-v", "error", "-f", "image2pipe", "-framerate", String(FPS), "-i", "-",
    "-i", path.join(root, "out/music.wav"), "-map", "0:v", "-map", "1:a",
    "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-r", String(FPS),
    "-af", "lowpass=f=16000", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], { stdio: ["pipe", "inherit", "inherit"] });
  const n = FPS * DUR;
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => window.render(t), i / FPS);
    const buf = await page.screenshot({ type: "png" });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
    if (i % 150 === 0) console.log(`[${f}] frame ${i}/${n}`);
  }
  ff.stdin.end();
  await new Promise((res, rej) => ff.on("close", c => (c === 0 ? res() : rej(new Error("ffmpeg exit " + c)))));
  console.log(`[${f}] -> ${out}`);
}

(async () => {
  const browser = await chromium.launch();
  await Promise.all(fmts.map(f => renderFormat(browser, f)));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
