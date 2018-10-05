
{% macro read_text(text, waitTimeMs=0) %}
    (function() {
        var msg = new SpeechSynthesisUtterance('{{ text }}');
        var voices = window.speechSynthesis.getVoices();
        msg.lang = 'ru-RU';

        msg.voice = voices[44];
        window.setTimeout(function () {
            speechSynthesis.speak(msg);
        }, {{ waitTimeMs}});
    })();
{% endmacro %}