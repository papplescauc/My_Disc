document.addEventListener("DOMContentLoaded", function() {
    console.log('hello world');

    document.getElementById('submit-button').addEventListener('click', function(mouseEvent) {
        /** @type {HTMLFormElement} */ const form = document.getElementById('main-form');
        form.reportValidity();
        mouseEvent.preventDefault();

        // display loading spinner

        // add course (call python code, wait for it to complete)

        // hide loading spinner

    });


});


