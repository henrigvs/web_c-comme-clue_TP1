let currentEnigmaIndex = 1;

function fetchEnigmaById(id) {
  fetch(`/enigmas/${id}`)
    .then((response) => response.json())
    .then((data) => {
      displayEnigma(data);
    })
    .catch((error) => {
      console.error(`Error fetching enigma with ID ${id}:`, error);
    });
}

function displayEnigma(enigma) {
  const enigmaDescription = document.getElementById("enigma-description");
  const enigmaHint = document.getElementById("enigma-hint");

  enigmaDescription.textContent = enigma.description;
  enigmaHint.textContent = enigma.hint;
}

function checkAnswer() {
  const userAnswerInput = document.getElementById("user-answer");
  const userAnswer = userAnswerInput.value.trim().toLowerCase();

  fetch(`/enigmas/${currentEnigmaIndex}`)
    .then((response) => response.json())
    .then((data) => {
      if (userAnswer === data.solution.toLowerCase()) {
        alert("Correct!");
        currentEnigmaIndex++;
        fetchEnigmaById(currentEnigmaIndex);
      } else {
        alert("Incorrect! Try again.");
      }
      userAnswerInput.value = ""; // Clear the input field
    })
    .catch((error) => {
      console.error(`Error fetching enigma with ID ${currentEnigmaIndex}:`, error);
    });
}

// Fetch the first enigma when the page loads
fetchEnigmaById(currentEnigmaIndex);

// Attach the checkAnswer function to the button
const checkAnswerButton = document.getElementById("check-answer-button");
checkAnswerButton.addEventListener("click", checkAnswer);
