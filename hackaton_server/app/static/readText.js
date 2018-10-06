function speakText(text, voice_id, wait_time) {

    speechSynthesis.onvoiceschanged = function() {
        voices = speechSynthesis.getVoices();
        var msg = new SpeechSynthesisUtterance(text);
        var voices = window.speechSynthesis.getVoices();
        msg.lang = 'ru-RU';

        msg.voice = voices[voice_id];
        window.setTimeout(function () {
            speechSynthesis.speak(msg);
        }, wait_time);
    };

}