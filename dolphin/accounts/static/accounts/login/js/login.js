document.querySelectorAll('.fields input').forEach(field => {
    field.addEventListener('focus', () => {
        event.target.style.background = 'black'
    })
    field.addEventListener('blur', () => {
        event.target.style.background = 'grey'
    })
})