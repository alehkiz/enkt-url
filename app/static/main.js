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

    buttonCopy.addEventListener('click', function () {
        var toast = new bootstrap.Toast(toastLiveExample)
    
        toast.show()
      })
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
