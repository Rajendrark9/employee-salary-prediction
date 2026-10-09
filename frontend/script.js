const form = document.getElementById("salaryForm");

const result = document.getElementById("result");
const salary = document.getElementById("salary");

const loading = document.getElementById("loading");
const error = document.getElementById("error");

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    result.classList.add("hidden");
    error.classList.add("hidden");
    loading.classList.remove("hidden");

    const employeeData = {
        age: Number(document.getElementById("age").value),

        experience: Number(
            document.getElementById("experience").value
        ),

        education: document.getElementById("education").value,

        department: document.getElementById("department").value,

        city: document.getElementById("city").value,

        previous_salary: Number(
            document.getElementById("previous_salary").value
        )
    };

    try {

        const response = await fetch("/predict", ...
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(employeeData)
            }
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Prediction failed"
            );
        }

        salary.textContent =
            "₹" +
            Math.round(data.predicted_salary)
                .toLocaleString("en-IN");

        result.classList.remove("hidden");

    } catch (err) {

        error.textContent = err.message;
        error.classList.remove("hidden");

    } finally {

        loading.classList.add("hidden");

    }
});