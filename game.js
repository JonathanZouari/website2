const WIN_LINES = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];

const cells = [...document.querySelectorAll(".cell")];
const statusEl = document.getElementById("status");
const scoreXEl = document.getElementById("score-x");
const scoreOEl = document.getElementById("score-o");
const scoreDrawEl = document.getElementById("score-draw");
const labelXEl = document.getElementById("label-x");
const labelOEl = document.getElementById("label-o");
const difficultyRow = document.querySelector(".difficulty-row");

const state = {
  board: Array(9).fill(""),
  current: "X",
  locked: false,
  mode: "pvp",
  difficulty: "easy",
  scores: { X: 0, O: 0, draw: 0 },
};

function winnerOf(board) {
  for (const line of WIN_LINES) {
    const [a, b, c] = line;
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      return { player: board[a], line };
    }
  }
  if (board.every(Boolean)) return { player: "draw", line: [] };
  return null;
}

function emptyIndexes(board) {
  return board.map((value, index) => (value ? null : index)).filter((index) => index !== null);
}

function minimax(board, player) {
  const result = winnerOf(board);
  if (result?.player === "O") return { score: 10 };
  if (result?.player === "X") return { score: -10 };
  if (result?.player === "draw") return { score: 0 };

  const moves = emptyIndexes(board).map((index) => {
    const next = board.slice();
    next[index] = player;
    const reply = minimax(next, player === "O" ? "X" : "O");
    return { index, score: reply.score };
  });

  if (player === "O") {
    return moves.reduce((best, move) => (move.score > best.score ? move : best));
  }
  return moves.reduce((best, move) => (move.score < best.score ? move : best));
}

function computerMove() {
  const empties = emptyIndexes(state.board);
  if (!empties.length) return;

  let index = empties[Math.floor(Math.random() * empties.length)];
  if (state.difficulty === "hard") {
    index = minimax(state.board, "O").index;
  }
  playAt(index);
}

function setStatus(text) {
  statusEl.textContent = text;
}

function render() {
  cells.forEach((cell, index) => {
    const mark = state.board[index];
    cell.querySelector(".mark-text").textContent = mark;
    cell.classList.toggle("x", mark === "X");
    cell.classList.toggle("o", mark === "O");
    cell.disabled = Boolean(mark) || state.locked;
    cell.setAttribute("aria-label", mark ? `משבצת ${index + 1}, ${mark}` : `משבצת ${index + 1}`);
  });
}

function highlight(line) {
  line.forEach((index) => cells[index].classList.add("win"));
}

function clearHighlight() {
  cells.forEach((cell) => cell.classList.remove("win"));
}

function updateScores() {
  scoreXEl.textContent = String(state.scores.X);
  scoreOEl.textContent = String(state.scores.O);
  scoreDrawEl.textContent = String(state.scores.draw);
}

function updateLabels() {
  const vsCpu = state.mode === "cpu";
  labelXEl.textContent = vsCpu ? "את/ה" : "שחקן X";
  labelOEl.textContent = vsCpu ? "מחשב" : "שחקן O";
  difficultyRow.hidden = !vsCpu;
}

function finishRound(result) {
  state.locked = true;
  if (result.player === "draw") {
    state.scores.draw += 1;
    setStatus("תיקו");
  } else {
    state.scores[result.player] += 1;
    highlight(result.line);
    if (state.mode === "cpu") {
      setStatus(result.player === "X" ? "ניצחת!" : "המחשב ניצח");
    } else {
      setStatus(`${result.player} ניצח`);
    }
  }
  updateScores();
}

function playAt(index) {
  if (state.locked || state.board[index]) return;

  state.board[index] = state.current;
  render();

  const result = winnerOf(state.board);
  if (result) {
    finishRound(result);
    return;
  }

  state.current = state.current === "X" ? "O" : "X";
  if (state.mode === "cpu" && state.current === "O") {
    setStatus("תור המחשב");
    state.locked = true;
    window.setTimeout(() => {
      state.locked = false;
      computerMove();
    }, 420);
    return;
  }

  setStatus(state.mode === "cpu" ? "התור שלך" : `תור של ${state.current}`);
}

function newRound() {
  state.board = Array(9).fill("");
  state.current = "X";
  state.locked = false;
  clearHighlight();
  render();
  setStatus(state.mode === "cpu" ? "התור שלך" : "תור של X");
}

function resetScores() {
  state.scores = { X: 0, O: 0, draw: 0 };
  updateScores();
  newRound();
}

cells.forEach((cell) => {
  cell.addEventListener("click", () => playAt(Number(cell.dataset.index)));
});

document.querySelectorAll("[data-mode]").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll("[data-mode]").forEach((el) => el.classList.remove("is-active"));
    button.classList.add("is-active");
    state.mode = button.dataset.mode;
    updateLabels();
    newRound();
  });
});

document.querySelectorAll("[data-difficulty]").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll("[data-difficulty]").forEach((el) => el.classList.remove("is-active"));
    button.classList.add("is-active");
    state.difficulty = button.dataset.difficulty;
    newRound();
  });
});

document.getElementById("new-round").addEventListener("click", newRound);
document.getElementById("reset-scores").addEventListener("click", resetScores);

updateLabels();
updateScores();
render();
