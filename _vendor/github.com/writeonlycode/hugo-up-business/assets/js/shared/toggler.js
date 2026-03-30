const addButtonList = document.querySelectorAll('[data-toggle-target]')

for (const addButton of addButtonList) {
  const addButtonTarget = document.querySelector(addButton.dataset.toggleTarget)
  const addButtonClass = addButton.dataset.toggleClass

  addButton.addEventListener('click', () => {
    for (const classToken of addButtonClass.split(' ')) {
      addButtonTarget.classList.toggle(classToken)
    }
  })
}
