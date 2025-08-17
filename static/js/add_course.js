document.addEventListener("DOMContentLoaded", function() {
    console.log('hello world');

    document.getElementById('submit-button').addEventListener('click', async function(mouseEvent) {
        /** @type {HTMLFormElement} */ const form = document.getElementById('main-form');
        form.reportValidity();
        mouseEvent.preventDefault();


        // display loading spinner

        // add course (call python code, wait for it to complete)
        let data = null;
        try {
            const response = await safeFetch('/python_function', 'Error calling python function');
            data = response['data'];
        }
        catch (err) {
            alert(err);
            throw err;
        }
        
        console.log(data);
        
        // hide loading spinner

    });


});



async function safeFetch(url, err_msg = 'Fetch Error', options = {}) {

    const response = await fetch(url, options);

    /** @type {Promise<Object>} */ let data = null;
    try {
        data = await response.json();
    }
    catch (jsonParseError) {
        throw new Error(`${err_msg}: Error parsing JSON during safeFetch: ${jsonParseError}`);
    }
    if (!response.ok) {
        throw new Error(`${err_msg}: ${data.error || 'Unexpected error'}: ${data.message || 'no further error info provided'}`);
    }

    return data;
}


