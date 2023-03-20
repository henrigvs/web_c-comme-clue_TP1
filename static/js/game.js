document.getElementById('sweetalert').addEventListener('click', function (){
    var hint = this.getAttribute('hint')
    Swal.fire({
        customClass: {
            popup: 'popup'
        },
        title: 'Hint',
        text: hint,
        confirmButtonClass: 'swal2-confirm button-cool',
        confirmButtonText: 'Cool',
        buttonsStyling: false,
    });
})
