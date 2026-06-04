function addTask() {

    let taskInput = document.getElementById("taskInput");
    let taskDate = document.getElementById("taskDate");
    let taskList = document.getElementById("taskList");

    if (taskInput.value === "") {
        alert("Please enter a task");
        return;
    }

    let li = document.createElement("li");

    li.innerHTML = `
        ${taskInput.value} - ${taskDate.value}
        <button onclick="completeTask(this)">Complete</button>
        <button onclick="editTask(this)">Edit</button>
        <button onclick="deleteTask(this)">Delete</button>
    `;

    taskList.appendChild(li);

    taskInput.value = "";
    taskDate.value = "";
}

function completeTask(button) {
    button.parentElement.style.textDecoration = "line-through";
}

function editTask(button) {
    let li = button.parentElement;
    let newTask = prompt("Edit Task", li.firstChild.textContent);

    if (newTask) {
        li.firstChild.textContent = newTask;
    }
}

function deleteTask(button) {
    button.parentElement.remove();
}