import speech_recognition as sr
class VoiceInput:
    def __init__(self, language='ko-KR', phrase_time_limit_sec=8, ambient_adjust_sec=0.5):
        self.language=language; self.limit=phrase_time_limit_sec; self.ambient=ambient_adjust_sec
        self.recognizer=sr.Recognizer()
    def listen_once(self):
        with sr.Microphone() as source:
            print('[VOICE] 주변 소음을 측정합니다.')
            self.recognizer.adjust_for_ambient_noise(source, duration=self.ambient)
            print('[VOICE] 명령을 말하세요.')
            audio=self.recognizer.listen(source, phrase_time_limit=self.limit)
        try:
            text=self.recognizer.recognize_google(audio, language=self.language)
            print('[STT]', text); return text
        except sr.UnknownValueError as exc: raise RuntimeError('음성을 이해하지 못했습니다.') from exc
        except sr.RequestError as exc: raise RuntimeError('STT 연결 실패: 텍스트 모드를 사용하세요.') from exc
