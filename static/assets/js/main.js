document.addEventListener("DOMContentLoaded", () => {
  const posts = document.querySelectorAll(".post");

  posts.forEach((post) => {
    const chatIcon = post.querySelector(".chat-icon");
    const commentSection = post.querySelector(".comment-section");
    const userIdInput = post.querySelector(".userIdInput");
    const usernameInput = post.querySelector(".username");
    const commentInput = post.querySelector(".commentText");
    const postButton = post.querySelector(".postComment");
    const commentsContainer = post.querySelector(".comments");
    const postId = post.querySelector(".post_id");

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
    const addComment = async () => {
      const userId = userIdInput.value.trim();
      const commentText = commentInput.value.trim();
      const post_id = postId.value.trim();
      const username = usernameInput.value.trim();

      if (userId !== "" && commentText !== "") {
        // Display the comment locally
        const commentElement = document.createElement("div");
        commentElement.classList.add("comment");
        commentElement.innerHTML = `<a href="/users/${userId}/profile/"><i>${username}</i></a><p>${commentText}</p>`;
        commentsContainer.appendChild(commentElement);
        commentsContainer.scrollTop = commentsContainer.scrollHeight;

        // Send the comment to the server
        try {
          const formData = new FormData();
          formData.append("userId", userId);
          formData.append("content", commentText);
          formData.append("post_id", post_id);

          const response = await fetch(`/`, {
            method: "POST",
            body: formData,
            headers: {
              "X-CSRFToken": getCookie("csrftoken"), // Add CSRF token if needed
            },
          });
        } catch (error) {
          console.error("Error posting comment: ", error);
        }

        // Clear the input fields
        commentInput.value = "";
      }
    };

    // Event listener for the post button
    postButton.addEventListener("click", addComment);

    // Enable the button only if both fields are filled
    const toggleButtonState = () => {
      postButton.disabled = commentInput.value.trim() === "";
    };

    userIdInput.addEventListener("input", toggleButtonState);
    commentInput.addEventListener("input", toggleButtonState);

    commentInput.addEventListener("keypress", (e) => {
      if (e.key === "Enter" && !postButton.disabled) {
        addComment();
      }
    });
  });
});

// Utility function to get CSRF token for POST requests
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    cookieValue = document.cookie.split("=")[1];
  }
  return cookieValue;
}
