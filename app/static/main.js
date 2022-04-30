let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl, {
        container: 'body',
        trigger : 'hover'
    });
})

window.onload = function(){
    var buttonCopy = document.getElementById("copy-button");
    var toastLiveExample = document.getElementById('liveToast')
    var toast = new bootstrap.Toast(toastLiveExample)
    if (buttonCopy !== null) {
        buttonCopy.addEventListener('click', function () {
            var copyText = document.getElementById("short-url");
            copyText.select();
            copyText.setSelectionRange(0, 99999);
            navigator.clipboard.writeText(copyText.value);
            toast.show()
        })
    }

    var elmCopy = document.getElementsByClassName('table-copy')
    for (var i = 0; i < elmCopy.length; i++){
        var id = elmCopy[i].id.split('copy-')[0]
        var elm = document.getElementById('copy-value-' + id)
        elmCopy[i].addEventListener('click', function(){
            console.log(this)
            console.log(this.id.split('copy-')[0])
            var id = this.id.split('copy-')[0]
            var elm = document.getElementById('copy-value-' + id)
            console.log(elm)
            // elm.select();
            // elm.setSelectionRange(0, 999999);
            navigator.clipboard.writeText(elm.href);
            toast.show()
        })
    }
}

// function copyValue() {
//     /* Get the text field */
//     var copyText = document.getElementById("short-url");

//     var buttonCopy = document.getElementById("copy-button");
//     var tooltip = bootstrap.Tooltip.getInstance(buttonCopy)
//     var toastLiveExample = document.getElementById('liveToast')
  
//     /* Select the text field */
//     copyText.select();
//     copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
//      /* Copy the text inside the text field */
//     navigator.clipboard.writeText(copyText.value);
//     console.log(buttonCopy)
//     tooltip.hide()
//     buttonCopy.setAttribute('data-bs-original-title', 'Copiado!!');
//     tooltip.show()
//     setTimeout(function(){
//         tooltip.hide()
//         buttonCopy.setAttribute('data-bs-original-title', 'Copiar');
//         tooltip.show()
//     }, 5000);
//     // tooltip.show()


//   } 
