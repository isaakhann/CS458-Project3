// SurveyPreview.tsx
import { useParams, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { doc, getDoc } from 'firebase/firestore';
import { db } from '../firebase-config';
import type { Question } from './SurveyDesigner';

type Answer = string | number | string[];

function SurveyPreview() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [questions, setQuestions] = useState<Question[]>([]);
  const [responses, setResponses] = useState<Record<number, Answer>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadSurvey = async () => {
      if (!id) {
        console.warn('No survey ID found in URL.');
        setLoading(false);
        return;
      }

      console.log('Attempting to fetch survey for ID:', id);
      const ref = doc(db, 'surveys', id);
      try {
        const snap = await getDoc(ref);
        if (snap.exists()) {
          const data = snap.data();
          console.log('Fetched survey data:', data);
          const loadedQuestions = Array.isArray(data.questions)
            ? data.questions
            : [];
          if (loadedQuestions.length === 0) {
            console.warn('Survey has no questions.');
          }
          setQuestions(loadedQuestions);
        } else {
          console.warn('No survey document found.');
          alert('Survey not found');
        }
      } catch (err) {
        console.error('Firestore fetch failed:', err);
      }

      setLoading(false);
    };

    loadSurvey();
  }, [id]);

  const handleChange = (qid: number, value: Answer) => {
    setResponses((prev) => ({ ...prev, [qid]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Responses:', responses);
    alert('Thanks for submitting the survey!');
    navigate('/');
  };

  if (loading) return <p style={{ textAlign: 'center' }}>Loading...</p>;

  if (!loading && questions.length === 0) {
    return (
      <p style={{ color: '#ccc', textAlign: 'center' }}>
        This survey has no questions.
      </p>
    );
  }

  return (
    <div className="designer-container">
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <h2>Survey Preview</h2>
        <button onClick={() => navigate('/')}>🏠 Home</button>
      </div>
      <form onSubmit={handleSubmit}>
        {questions.map((q) => (
          <div key={q.id} className="question-card">
            <label>
              {q.label}
              {q.required && ' *'}
            </label>
            {q.type === 'text' && (
              <input
                type="text"
                required={q.required}
                onChange={(e) => handleChange(q.id, e.target.value)}
              />
            )}
            {q.type === 'multiple-choice' &&
              q.options.map((opt, i) => (
                <label key={i} style={{ display: 'block' }}>
                  <input
                    type="radio"
                    name={`q-${q.id}`}
                    value={opt}
                    required={q.required}
                    onChange={() => handleChange(q.id, opt)}
                  />{' '}
                  {opt}
                </label>
              ))}
            {q.type === 'dropdown' && (
              <select
                required={q.required}
                onChange={(e) => handleChange(q.id, e.target.value)}
              >
                <option value="">Select an option</option>
                {q.options.map((opt, i) => (
                  <option key={i} value={opt}>
                    {opt}
                  </option>
                ))}
              </select>
            )}
            {q.type === 'checkbox' &&
              q.options.map((opt, i) => (
                <label key={i} style={{ display: 'block' }}>
                  <input
                    type="checkbox"
                    value={opt}
                    onChange={(e) => {
                      const isChecked = e.target.checked;
                      const prev = (responses[q.id] as string[]) || [];
                      handleChange(
                        q.id,
                        isChecked
                          ? [...prev, opt]
                          : prev.filter((v) => v !== opt)
                      );
                    }}
                  />{' '}
                  {opt}
                </label>
              ))}
            {q.type === 'rating' &&
              [1, 2, 3, 4, 5].map((num) => (
                <label key={num} style={{ marginRight: '10px' }}>
                  <input
                    type="radio"
                    name={`q-${q.id}`}
                    value={num}
                    required={q.required}
                    onChange={() => handleChange(q.id, num)}
                  />{' '}
                  {num}
                </label>
              ))}
          </div>
        ))}
        <button type="submit" style={{ marginTop: '20px' }}>
          Submit Survey
        </button>
      </form>
    </div>
  );
}

export default SurveyPreview;
