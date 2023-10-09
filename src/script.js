$(document).ready(function() {
    const imgContainer = $('.card_img');
    const heading = $('.heading');
    const para = $('.para');
    let currentIndex = 0; // To keep track of the current user index

    // Function to load and display user data with GSAP animation
    function loadUserData(index) {
        $.getJSON('src/allowedUsers.json', function(data) {
            if (index >= 0 && index < data.length) {
                const user = data[index];
                const img = $('<img>');
                img.attr('src', 'imgs/' + user.Image);
                // Create a timeline for animations
                const tl = gsap.timeline();

                // Add animations to the timeline
                tl.to([imgContainer, heading, para], { opacity: 0, x: -50, duration: 0.5, onComplete: function() {
                    // Update the content and image
                    imgContainer.empty().append(img);
                    imgContainer.removeClass('loading');
                    heading.text(user.Name);
                    heading.removeClass('loading');
                    para.text(user.Description);
                    para.removeClass('loading');

                    // Reset position and opacity
                    imgContainer.css({ opacity: 0, x: 50 });

                    // Apply a fade-in and slide-in animation
                    tl.to([imgContainer, heading, para], { opacity: 1, x: 0, duration: 0.5 });
                } });

                currentIndex = index;
            }
        });
    }

    // Initial loading of user data
    loadUserData(currentIndex);

    // Handle "prev" button click
    $('.prev').click(function() {
        if (currentIndex > 0) {
            loadUserData(currentIndex - 1);
        }
    });

    // Handle "next" button click
    $('.next').click(function() {
        $.getJSON('src/allowedUsers.json', function(data) {
            if (currentIndex < data.length - 1) {
                loadUserData(currentIndex + 1);
            }
        });
    });
});
