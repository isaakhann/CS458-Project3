// AllSurveys.tsx
import { useEffect, useState } from 'react';
import { collection, getDocs } from 'firebase/firestore';
import { db } from '../firebase-config';
import { useNavigate } from 'react-router-dom';

interface SurveyMeta {
  id: string;
  createdAt: string;
  questionCount: number;
}

function AllSurveys() {
  const [surveys, setSurveys] = useState<SurveyMeta[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchSurveys = async () => {
      const snapshot = await getDocs(collection(db, 'surveys'));
      const data: SurveyMeta[] = snapshot.docs.map((doc) => {
        const d = doc.data();
        return {
          id: doc.id,
          createdAt: d.createdAt?.toDate().toLocaleString() || 'Unknown date',
          questionCount: d.questions?.length || 0,
        };
      });
      setSurveys(data);
    };
    fetchSurveys();
  }, []);

  return (
    <div className="designer-container">
      <h2>All Surveys</h2>
      {surveys.length === 0 ? (
        <p>No surveys found.</p>
      ) : (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {surveys.map((survey) => (
            <li
              key={survey.id}
              style={{
                background: '#2a2a2a',
                padding: '16px',
                borderRadius: '10px',
                marginBottom: '16px',
                cursor: 'pointer',
                transition: 'background 0.2s',
              }}
              onClick={() => navigate(`/survey/${survey.id}`)}
            >
              <strong>ID:</strong> {survey.id}
              <br />
              <strong>Questions:</strong> {survey.questionCount}
              <br />
              <strong>Created:</strong> {survey.createdAt}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default AllSurveys;
