const openDeleteTaskModal = (project_id, task_id) => {
    const modal = document.getElementById("deleteModal");
    const confirmDelete = document.getElementById("confirmDelete");
    const cancelDeleteButton = document.getElementById("cancelDeleteButton");

    modal.classList.remove("hidden");

    confirmDelete.href=`/tasks/${project_id}/delete/${task_id}`;

    cancelDeleteButton.onclick = () => {
        modal.classList.add("hidden");
    }
};

const openCreateTaskModal = () => {
    const modal = document.getElementById("createTaskModal");
    const cancelCreateButton = document.getElementById("cancelCreateButton");

    modal.classList.remove("hidden");

    cancelCreateButton.addEventListener("click", (e) => {
        e.preventDefault();
        
        modal.classList.add("hidden");
    });
};