function addSeccion(){
    var section = document.getElementById('section');
    section.innerHTML= '<input class="form-control {% if form.title.errors %}is-invalid{% endif %}" type="text" name="Section" placeholder="Section Name">';
}

