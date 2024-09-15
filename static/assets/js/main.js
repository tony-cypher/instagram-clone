document.addEventListener("DOMContentLoaded", () => {
  const posts = document.querySelectorAll(".post");

  posts.forEach((post) => {
    const chatIcon = post.querySelector(".chat-icon");
    const commentSection = post.querySelector(".comment-section");
    const commentInput = post.querySelector(".commentText");
    const postButton = post.querySelector(".postComment");
    const commentsContainer = post.querySelector(".comments");

    // Toggle visibility of the comment section for each post
    chatIcon.addEventListener("click", () => {
      if (commentSection.style.display === "block") {
        fadeOutCommentSection(commentSection);
      } else {
        fadeInCommentSection(commentSection);
      }
    });

    // Function to show the comment section with animation
    const fadeInCommentSection = (section) => {
      section.style.display = "block";
      setTimeout(() => {
        section.style.opacity = "1";
        section.style.transform = "translateY(0)";
      }, 10);
    };

    // Function to hide the comment section with animation
    const fadeOutCommentSection = (section) => {
      section.style.opacity = "0";
      section.style.transform = "translateY(20px)";
      setTimeout(() => {
        section.style.display = "none";
      }, 500); // Match the transition duration
    };

    // Close the comment section if clicked outside
    document.addEventListener("click", (event) => {
      if (
        !commentSection.contains(event.target) &&
        !chatIcon.contains(event.target) &&
        commentSection.style.display === "block"
      ) {
        fadeOutCommentSection(commentSection);
      }
    });

    // Function to add a new comment
    const addComment = () => {
      const commentText = commentInput.value.trim();

      if (commentText !== "") {
        // Create a new comment element
        const commentElement = document.createElement("div");
        commentElement.classList.add("comment");
        commentElement.innerHTML = `<p>${commentText}</p>`;

        // Add the comment to the container
        commentsContainer.appendChild(commentElement);

        // Scroll to the bottom to show the new comment
        commentsContainer.scrollTop = commentsContainer.scrollHeight;

        // Clear the input field
        commentInput.value = "";
      }
    };

    // Event listener for the post button
    postButton.addEventListener("click", addComment);

    // Enable the button only if there's text
    commentInput.addEventListener("input", () => {
      postButton.disabled = commentInput.value.trim() === "";
    });

    // Enable posting a comment with the Enter key
    commentInput.addEventListener("keypress", (e) => {
      if (e.key === "Enter") {
        addComment();
      }
    });
  });
});
