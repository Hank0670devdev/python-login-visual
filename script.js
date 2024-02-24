// Simulate login success
var loggedIn = true;

window.onload = function() {
  if (loggedIn) {
    showOSInterface();
  }
};

function showOSInterface() {
  document.getElementById('os-container').style.display = 'block';
}
