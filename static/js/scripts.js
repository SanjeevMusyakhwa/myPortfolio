let words = document.querySelectorAll(".word"); // Use querySelectorAll to select all elements with the class "word"
words.forEach((word) => {
  let letters = word.textContent.split(""); // Split the text content into individual letters
  word.textContent = ""; // Clear the text content
  letters.forEach((letter) => {
    let span = document.createElement("span"); // Create a span element for each letter
    span.textContent = letter; // Set the letter as the text content of the span
    span.className = "letter"; // Add the class "letter" to the span
    word.append(span); // Append the span to the word element
  });
});

let currentWordIndex = 0;
let maxWordIndex = words.length - 1; // Use words.length to calculate the max index
words[currentWordIndex].style.opacity = "1"; // Set the opacity of the first word

let changeText = () => {
  let currentWord = words[currentWordIndex];
  let nextWord = currentWordIndex === maxWordIndex ? words[0] : words[currentWordIndex + 1];

  // Fade out current word letters
  Array.from(currentWord.children).forEach((letter, i) => {
    setTimeout(() => {
      letter.className = "letter out";
    }, i * 80);
  });

  // Show next word letters
  nextWord.style.opacity = "1";
  Array.from(nextWord.children).forEach((letter, i) => {
    letter.className = "letter behind"; // Set initial class
    setTimeout(() => {
      letter.className = "letter in";
    }, 340 + i * 80);
  });

  // Update the current word index
  currentWordIndex = currentWordIndex === maxWordIndex ? 0 : currentWordIndex + 1;
};

// Start the animation cycle
changeText();
setInterval(changeText, 3000);



// Circle Skill

const circles = document.querySelectorAll('.circle');
circles.forEach(elem => {
  var dots = elem.getAttribute('data-dots');
  var marked = elem.getAttribute('data-percent');
  var percent = Math.floor((dots * marked) / 100);
  var points = "";
  var rotate = 360 / dots;

  for (let i = 0; i < dots; i++) {
    points += `<div class="points" style="--i:${i}; --rot:${rotate}deg"></div>`;
  }
  elem.innerHTML = points;

  const pointsMarked = elem.querySelectorAll('.points');
  for (let i = 0; i < percent; i++) {
    pointsMarked[i].classList.add('marked');
  }
});


// Mixitup protfolio section 

// var mixer = mixitup(".portfolio-gallery");

let menuLi = document.querySelectorAll('header ul li a');
let section = document.querySelectorAll('section');

function activeMenu(){
  let len = section.length;
  while(--len && window.scrollY + 97 < section[len].offsetTop){}
  menuLi.forEach(sec => sec.classList.remove("active"));
  menuLi[len].classList.add("active");
}

activeMenu();
window.addEventListener("scroll",activeMenu);

// Sticky Navbar 

const header = document.querySelector("header");
window.addEventListener("scroll", function(){
  header.classList.toggle("sticky", window.scrollY > 50)
})


// Navlist open
let menuIcon = document.querySelector("#menu-icon");
let navlist = document.querySelector(".navlist");

menuIcon.onclick =() => {
  menuIcon.classList.toggle("bx-x");
  navlist.classList.toggle("open");
}

window.onscroll =() => {
  menuIcon.classList.remove("bx-x");
  navlist.classList.remove("open");
}


// Parallax 

const observer = new IntersectionObserver((entries) =>{
  entries.forEach((entry)=>{
    if(entry.isIntersecting){
      entry.target.classList.add("show-items");
    }
    else{
      entry.target.classList.remove("show-items");
    }
  });
});

const scrollScale = document.querySelectorAll(".scroll-scale");
scrollScale.forEach((el)=>observer.observe(el));

const scrollBottom = document.querySelectorAll(".scroll-bottom");
scrollBottom.forEach((el)=>observer.observe(el));

const scrollTop = document.querySelectorAll(".scroll-top");
scrollTop.forEach((el)=>observer.observe(el));

// Thank YOu Message 

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");
  const successMessage = document.getElementById("successMessage");

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    // Send the form data using Fetch API
    const formData = new FormData(form);
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    fetch(form.action, {
      method: "POST",
      body: formData,
      headers: {
        "X-CSRFToken": csrfToken,  // Use correct token handling
      },
    })
      .then((response) => {
        if (response.ok) {
          // Display success message
          successMessage.style.display = "block";

          // Clear the form
          form.reset();

          // Optionally hide the success message after a few seconds
          setTimeout(() => {
            successMessage.style.display = "none";
          }, 5000);
        } else {
          response.json().then(data => {
            alert(data.error || "An error occurred. Please try again.");
          });
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
      });
  });
});
