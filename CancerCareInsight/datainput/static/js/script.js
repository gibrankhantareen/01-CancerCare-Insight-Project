document.addEventListener("DOMContentLoaded", function() {
    const dataInputForm = document.getElementById("data-input-form");

    dataInputForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = new FormData(dataInputForm);
        const data = {};

        formData.forEach((value, key) => {
            data[key] = value;
        });

        console.log("Collected Data:", data);

        // TODO: Process the data as needed (e.g., send to server, store in local storage, etc.)
    });
});
