function speakText(text, wait_time) {
    var dfd = jQuery.Deferred();
    speechSynthesis.onvoiceschanged = function () {
        voices = speechSynthesis.getVoices();
        var msg = new SpeechSynthesisUtterance(text);
        var voices = window.speechSynthesis.getVoices();
        msg.lang = 'ru-RU';

        msg.voice = voices[window.default_voice_id];
        speechSynthesis.speak(msg);
        window.setTimeout(function () {
            dfd.resolve(true);
        }, wait_time);
        speechSynthesis.onvoiceschanged = null
    };
    return dfd.promise()

}