import { signOut } from 'firebase/auth';
import { auth } from '../firebase-config';
import { useNavigate } from 'react-router-dom';
import SurveyForm from './SurveyForm';

function WelcomePage({ user }: { user: import('firebase/auth').User }) {
  const navigate = useNavigate();

  const handleLogout = async () => {
    await signOut(auth);
    navigate('/');
  };

  return (
    <>
      {/* 🔵 Navbar */}
      <div
        style={{
          width: '100%',
          padding: '16px 24px',
          backgroundColor: '#2c2c2c',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          borderBottom: '1px solid #444',
        }}
      >
        <h3 style={{ margin: 0, color: '#f1f1f1' }}>Survey Dashboard</h3>
        <div style={{ display: 'flex', gap: '12px' }}>
          <button onClick={() => navigate('/designer')}>Create Survey</button>
          <button onClick={() => navigate('/surveys')}>All Surveys</button>
          <button onClick={handleLogout}>Logout</button>
        </div>
      </div>

      {/* 🔵 Welcome content */}
      <div className="welcome-page">
        <div className="welcome-content">
          <h1>Welcome, {user.email || 'User'}!</h1>
          <h2>Survey:</h2>
          <div className="form-wrapper">
            <SurveyForm />
          </div>
        </div>
      </div>
    </>
  );
}

export default WelcomePage;
