import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from 'react-router-dom';
import { useEffect, useState } from 'react';
import { auth } from './firebase-config';
import { onAuthStateChanged, User } from 'firebase/auth';
import WelcomePage from './components/WelcomePage';
import SurveyDesigner from './components/SurveyDesigner';
import './App.css';
import AllSurveys from './components/AllSurveys';
import AuthScreen from './components/AuthScreen';
import SurveyPreview from './components/SurveyPreview';

function App() {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
    });
    return () => unsubscribe();
  }, []);

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={user ? <Navigate to="/welcome" /> : <AuthScreen />}
        />
        <Route
          path="/welcome"
          element={user ? <WelcomePage user={user} /> : <Navigate to="/" />}
        />
        <Route
          path="/designer"
          element={user ? <SurveyDesigner /> : <Navigate to="/" />}
        />
        <Route path="/survey/:id" element={<SurveyPreview />} />
        <Route path="/surveys" element={<AllSurveys />} />
      </Routes>
    </Router>
  );
}

export default App;
