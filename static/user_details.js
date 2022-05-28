function enable()
{
    var field = document.getElementById('add_value')
    field.disabled = false;
    field.style.border = '2px solid #295D09'
}

function save()
{
    var field = document.getElementById('add_value')
    // field.disabled = true;
    field.style.border = '0'
}