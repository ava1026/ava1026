// HTML → PDF。用页面自己的 @media print 样式（强制浅色、解除 SVG min-width、控制分页）。
//
// 仓库里没装 playwright —— 在装了 playwright 的目录下运行：
//   cd <装了 playwright 的目录> && node /home/user/ava1026/docs/_build/render-pdf.mjs <名字> "<页脚文案>"
// 例：
//   node .../render-pdf.mjs fomo-growth-loop  "FOMO 增长闭环 · 竞品情报 · 内部使用"
//   node .../render-pdf.mjs gmgn-counterplay  "GMGN App 产品侧打法 · 内部使用"
//
// Chromium 用系统预装的那份。注意目录带版本号，直接写 /opt/pw-browsers/chromium 是空壳。
import { chromium } from 'playwright';
import { readdirSync } from 'node:fs';

const DOCS = '/home/user/ava1026/docs';
const name = process.argv[2] ?? 'fomo-growth-loop';
const label = process.argv[3] ?? name;
const asOf = process.argv[4] ?? '2026-08-11';

// /opt/pw-browsers 下的 chromium 目录带版本后缀（chromium-1194 等），扫出来用。
const root = '/opt/pw-browsers';
const dir = readdirSync(root).find(d => /^chromium-\d+$/.test(d)) ?? 'chromium';
const executablePath = `${root}/${dir}/chrome-linux/chrome`;

const b = await chromium.launch({ executablePath });
const p = await b.newPage({ colorScheme: 'light' });
await p.goto(`file://${DOCS}/${name}.html`, { waitUntil: 'networkidle' });
await p.emulateMedia({ media: 'print', colorScheme: 'light' });
await p.waitForTimeout(500);
await p.pdf({
  path: `${DOCS}/${name}.pdf`,
  format: 'A4',
  printBackground: true,
  displayHeaderFooter: true,
  margin: { top: '14mm', right: '12mm', bottom: '16mm', left: '12mm' },
  headerTemplate: '<div></div>',
  footerTemplate: `<div style="width:100%;font-size:7.5pt;color:#6b7680;padding:0 12mm;
      font-family:-apple-system,'PingFang SC',sans-serif;display:flex;justify-content:space-between;">
      <span>${label} · 数据截止 ${asOf}</span>
      <span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
});
await b.close();
console.log(`pdf written: ${DOCS}/${name}.pdf`);
