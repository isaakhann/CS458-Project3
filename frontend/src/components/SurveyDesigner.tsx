import { useState } from 'react';
import { db } from '../firebase-config';
import { addDoc, collection } from 'firebase/firestore';

export type QuestionType =
  | 'text'
  | 'multiple-choice'
  | 'dropdown'
  | 'checkbox'
  | 'rating';

export interface Question {
  id: number;
  type: QuestionType;
  label: string;
  options: string[];
  required: boolean;
}

const defaultQuestion = (): Question => ({
  id: Date.now(),
  type: 'multiple-choice',
  label: '',
  options: ['Option 1'],
  required: false,
});

function SurveyDesigner() {
  const [questions, setQuestions] = useState<Question[]>([]);

  const addQuestion = () => {
    setQuestions((prev) => [...prev, defaultQuestion()]);
  };

  const updateQuestion = <K extends keyof Question>(
    id: number,
    key: K,
    value: Question[K]
  ) => {
    setQuestions((prev) =>
      prev.map((q) => (q.id === id ? { ...q, [key]: value } : q))
    );
  };

  const updateOption = (qid: number, idx: number, value: string) => {
    setQuestions((prev) =>
      prev.map((q) =>
        q.id === qid
          ? {
              ...q,
              options: q.options.map((opt, i) => (i === idx ? value : opt)),
            }
          : q
      )
    );
  };

  const addOption = (qid: number) => {
    setQuestions((prev) =>
      prev.map((q) =>
        q.id === qid
          ? { ...q, options: [...q.options, `Option ${q.options.length + 1}`] }
          : q
      )
    );
  };

  const deleteOption = (qid: number, idx: number) => {
    setQuestions((prev) =>
      prev.map((q) =>
        q.id === qid
          ? { ...q, options: q.options.filter((_, i) => i !== idx) }
          : q
      )
    );
  };

  const deleteQuestion = (id: number) => {
    setQuestions((prev) => prev.filter((q) => q.id !== id));
  };

  const saveSurvey = async () => {
    try {
      const docRef = await addDoc(collection(db, 'surveys'), {
        questions,
        createdAt: new Date(),
      });
      alert(`Survey saved! Share this ID: ${docRef.id}`);
    } catch (e) {
      console.error('Error saving survey:', e);
      alert('Failed to save survey.');
    }
  };

  return (
    <div className="designer-container">
      <h2>Survey Designer</h2>
      <button onClick={addQuestion} className="add-question-btn">
        + Add Question
      </button>
      {questions.map((q) => (
        <div key={q.id} className="question-card">
          <div className="question-header">
            <input
              type="text"
              placeholder="Untitled question"
              value={q.label}
              onChange={(e) => updateQuestion(q.id, 'label', e.target.value)}
            />
            <select
              value={q.type}
              onChange={(e) =>
                updateQuestion(q.id, 'type', e.target.value as QuestionType)
              }
            >
              <option value="text">Short Answer</option>
              <option value="multiple-choice">Multiple Choice</option>
              <option value="dropdown">Dropdown</option>
              <option value="checkbox">Checkboxes</option>
              <option value="rating">Rating</option>
            </select>
          </div>

          {['multiple-choice', 'dropdown', 'checkbox'].includes(q.type) && (
            <>
              {q.options.map((opt, i) => (
                <div key={i} className="option-input">
                  <input
                    type="text"
                    value={opt}
                    onChange={(e) => updateOption(q.id, i, e.target.value)}
                    placeholder={`Option ${i + 1}`}
                  />
                  {q.options.length > 1 && (
                    <button onClick={() => deleteOption(q.id, i)}>✕</button>
                  )}
                </div>
              ))}
              <button onClick={() => addOption(q.id)} className="subtle-btn">
                + Add Option
              </button>
            </>
          )}

          {q.type === 'rating' && (
            <p className="info-text">Rating scale: 1–5</p>
          )}
          {q.type === 'text' && (
            <p className="info-text">User will provide short text response.</p>
          )}

          <div className="question-footer">
            <label className="toggle-label">
              <input
                type="checkbox"
                checked={q.required}
                onChange={(e) =>
                  updateQuestion(q.id, 'required', e.target.checked)
                }
              />
              <span className="slider" />
              Required
            </label>
            <button onClick={() => deleteQuestion(q.id)}>🗑 Delete</button>
          </div>
        </div>
      ))}
      <button
        onClick={saveSurvey}
        className="add-question-btn"
        style={{ marginTop: '16px' }}
      >
        ✅ Save Survey to Firebase
      </button>
    </div>
  );
}

export default SurveyDesigner;
