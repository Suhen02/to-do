function openTask(){
    const item=document.getElementById('forms')
    const btn=document.getElementById('btn')
    item.classList.add('swithClass')
    btn.innerText="close"
}
function closetask(){
    const item=document.getElementById('forms')
    const btn=document.getElementById('btn')
    item.classList.remove('swithClass')
    btn.innerText="Add task"
}
function displayData(){
    const item=document.getElementById('displayData')
    item.classList.add('display_data')
}
function markAsDone(button) {
    // Change task appearance
    const taskItem = button.parentElement;
    taskItem.style.textDecoration = "line-through";
    taskItem.style.color = "gray";

    // Disable the button after marking the task
    button.disabled = true;
    button.innerText = "Done!";

    // Optional: Add functionality to update progress or send data to server
    console.log("Task marked as done!");
}