// 需要 playwright。仓库里没装 —— 在装有 playwright 的目录下运行，例如：
//   cd <装了 playwright 的目录> && node /home/user/ava1026/docs/_build/render-pdf.mjs
// 或先在本目录 npm i playwright。Chromium 用系统预装的 /opt/pw-browsers/chromium。
import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ colorScheme: 'light' });
await p.goto('file:///home/user/ava1026/docs/fomo-growth-loop.html', { waitUntil:'networkidle' });
await p.emulateMedia({ media: 'print', colorScheme: 'light' });
await p.waitForTimeout(500);
await p.pdf({
  path: '/home/user/ava1026/docs/fomo-growth-loop.pdf',
  format: 'A4',
  printBackground: true,
  displayHeaderFooter: true,
  margin: { top:'14mm', right:'12mm', bottom:'16mm', left:'12mm' },
  headerTemplate: '<div></div>',
  footerTemplate: `<div style="width:100%;font-size:7.5pt;color:#6b7680;padding:0 12mm;
      font-family:-apple-system,'PingFang SC',sans-serif;display:flex;justify-content:space-between;">
      <span>FOMO 增长闭环 · 竞品情报 · 内部使用 · 数据截止 2026-08-11</span>
      <span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
});
await b.close();
console.log('pdf written');
