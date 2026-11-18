// Helpers for drawing tensors and layer stacks in slide SVGs (Claude Docs widgets).
// Paste the ones you need above `export default`. They draw shapes only: every
// label stays a literal <text data-claude-text-id='...'> written by hand.

// Matrix as a grid of cells, e.g. hidden states T x d. `dim` greys out the first `skip` rows
// (such as a BOS token excluded from pooling).
const grid = (x, y, rows, cols, cell, fill, skip = 0, dim = '#D9D9D9') => Array.from({length: rows}, (_, r) => Array.from({length: cols}, (_, c) => <rect key={`${r}-${c}`} x={x + c * cell} y={y + r * cell} width={cell - 1} height={cell - 1} fill={r < skip ? dim : fill}/>));

// Vector as one row of cells (e.g. a pooled hidden state).
const vec = (x, y, n, cell, h, fill) => Array.from({length: n}, (_, i) => <rect key={i} x={x + i * cell} y={y} width={cell - 1} height={h} fill={fill}/>);

// Stack of n layers drawn as slanted slabs, bottom (layer 1) to top. Layers listed in `sel` use `on`.
const slabs = (x, yBottom, n, sel, on, off, w = 130, skew = 24, step = 10, thick = 8) => Array.from({length: n}, (_, k) => { const i = k + 1, y = yBottom - i * step; return <polygon key={i} points={`${x},${y} ${x + w},${y} ${x + w + skew},${y - thick} ${x + skew},${y - thick}`} fill={sel.includes(i) ? on : off} stroke='#FFFFFF' strokeWidth='1'/>; });

// Segments stacked vertically (e.g. concatenated vectors); colours alternate.
const segs = (x, y, n, w, h, a, b) => Array.from({length: n}, (_, i) => <rect key={i} x={x} y={y + i * (h + 2)} width={w} height={h} fill={i % 2 === 0 ? a : b}/>);

// Bars on a baseline (e.g. class probabilities). The tallest bar uses `hot`.
const bars = (x, base, heights, w, gap, c, hot) => { const top = Math.max(...heights); return heights.map((h, i) => <rect key={i} x={x + i * (w + gap)} y={base - h} width={w} height={h} fill={h === top ? hot : c}/>); };
