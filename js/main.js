
function apply() {
    // Add new class to existing classes
    var p = document.querySelector("table");
    p.classList.add("table");
    p.classList.add("table-hover");
    p.classList.add("table-sm");


    var q = document.querySelector("a");
    q.classList.replace('titlelink', 'link-secondary')

    Array.prototype.forEach.call(document.getElementsByTagName('a'), function (element) {
        element.classList.replace('titlelink', 'link-secondary');
    });



};
