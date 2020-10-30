window.addEventListener('load', main);

function main() {
  function toggleApplianceState(e) {
    var id = e.path[1].id;

    var http = new XMLHttpRequest();
    
    http.onreadystatechange = function() {
        if(this.readyState === 4 && this.status === 200) {
          if(JSON.parse(this.responseText).status === true) {
            if(e.path[1].hasAttribute('data-active')) {
              e.path[1].removeAttribute('data-active')
            } else {
              e.path[1].setAttribute('data-active', 'active')
            }
          }
        }
    }
    
    http.open("GET", `/appliance/toggle/${id}`, true);
    http.send();
  }


  var appliances = document.getElementsByClassName('appliance');
  for(i=0; i < appliances.length; i++) {
    appliances[i].addEventListener('click', toggleApplianceState);
  }
}