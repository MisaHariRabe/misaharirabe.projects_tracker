const openDeleteModal = (project_id) => {
    const modal = document.getElementById("deleteModal");
    const confirmDelete = document.getElementById("confirmDelete");
    const cancelDeleteButton = document.getElementById("cancelDeleteButton");

    modal.classList.remove("hidden");

    confirmDelete.href = `/projects/delete/${project_id}`;

    cancelDeleteButton.onclick = () => {
        modal.classList.add("hidden");
    }
};

const openCreateProjectModal = () => {
    const modal = document.getElementById("createProjectModal");
    const cancelCreateButton = document.getElementById("cancelCreateButton");

    modal.classList.remove("hidden");

    cancelCreateButton.addEventListener("click", (e) => {
        e.preventDefault();
        
        modal.classList.add("hidden");
    });
};