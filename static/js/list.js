document.addEventListener('DOMContentLoaded', function() {
        var buttons = document.getElementsByClassName('btn-list');
        for (var i = 0; i < buttons.length; i++) {
            buttons[i].addEventListener('click', function() {
                var hint = this.getAttribute('hint');
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
            });
        }
    });


function changeDifficulty(n){
    if(n >= 0){
        n = n + 1;
    }
    return n;
}
