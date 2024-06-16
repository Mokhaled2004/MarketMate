const tabBtn = document.querySelectorAll(".tab");
const tab = document.querySelectorAll(".tabShow");

function tabs(panelIndex) {
    tab.forEach(function(node) {
        node.style.display = "none";
    });
    tab[panelIndex].style.display = "block";
}

tabs(0);

$(".tab").click(function(){
    $(this).addClass("active").siblings().removeClass("active");
});

// Example input behavior
document.addEventListener("DOMContentLoaded", function() {
    const inputs = document.querySelectorAll(".input");
    
    inputs.forEach(function(input) {
        const placeholderText = input.getAttribute("placeholder");
        
        input.addEventListener("focus", function() {
            if (this.value === '') {
                this.placeholder = placeholderText;
            }
        });

        input.addEventListener("input", function() {
            if (this.value !== '') {
                this.placeholder = '';
            }
        });
    });
});
