document.getElementById('btn-start').addEventListener('click', function() {
    var videoStream = document.getElementById('video-stream');
    videoStream.src = videoStream.getAttribute('data-url');
    document.getElementById('btn-start').style.display = 'none';
    document.getElementById('btn-stop').style.display = 'block';
});

document.getElementById('btn-stop').addEventListener('click', function() {
    var videoStream = document.getElementById('video-stream');
    videoStream.src = '';
    document.getElementById('btn-start').style.display = 'block';
    document.getElementById('btn-stop').style.display = 'none';
});