let questions = [];
let selectedAnswers = [];

async function loadQuestions() {
    const res = await fetch("/questions");
    questions = await res.json();

    const quizDiv = document.getElementById("quiz");
    quizDiv.innerHTML = "";

    questions.forEach((q, index) => {
        let html = `<p>${q.question}</p>`;

        q.options.forEach(opt => {
            html += `
                <input type="radio" name="q${index}" value="${opt}" 
                onchange="selectAnswer(${index}, '${opt}')"> ${opt}<br>
            `;
        });

        quizDiv.innerHTML += html;
    });
}

function selectAnswer(index, answer) {
    selectedAnswers[index] = answer;
}

async function submitQuiz() {
    const username = document.getElementById("username").value;

    const res = await fetch("/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            answers: selectedAnswers
        })
    });

    const data = await res.json();

    document.getElementById("result").innerText =
        `${data.username}, your score: ${data.score}/${data.total}`;

    loadScores();
}

async function loadScores() {
    const res = await fetch("/scores");
    const data = await res.json();

    const board = document.getElementById("scoreboard");
    board.innerHTML = "";

    data.forEach(s => {
        board.innerHTML += `<li>${s.username} - ${s.score}</li>`;
    });
}

// Load on start
loadQuestions();
loadScores();
