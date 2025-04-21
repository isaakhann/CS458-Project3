import { useState } from 'react';
import {
  GoogleAuthProvider,
  GithubAuthProvider,
  signInWithPopup,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
} from 'firebase/auth';
import { auth } from '../firebase-config';

function AuthScreen() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleEmailAuth = async () => {
    setError(null);
    if (!email || !password) {
      setError('Email and password required.');
      return;
    }

    try {
      if (isRegistering) {
        await createUserWithEmailAndPassword(auth, email, password);
      } else {
        await signInWithEmailAndPassword(auth, email, password);
      }
    } catch (e) {
      if (e instanceof Error) {
        setError(e.message);
      } else {
        setError('An unknown error occurred.');
      }
    }
  };

  const handleGoogle = async () => {
    const provider = new GoogleAuthProvider();
    await signInWithPopup(auth, provider);
  };

  const handleGitHub = async () => {
    const provider = new GithubAuthProvider();
    provider.addScope('user:email');
    await signInWithPopup(auth, provider);
  };

  return (
    <div className="auth-container">
      <h2>{isRegistering ? 'Sign Up' : 'Sign In'}</h2>
      {error && <p className="error">{error}</p>}

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleEmailAuth}>
        {isRegistering ? 'Sign Up' : 'Sign In'}
      </button>

      <p>
        {isRegistering ? 'Already have an account?' : "Don't have an account?"}
        <button onClick={() => setIsRegistering(!isRegistering)}>
          {isRegistering ? 'Sign In' : 'Sign Up'}
        </button>
      </p>

      <button onClick={handleGoogle}>Sign in with Google</button>
      <button onClick={handleGitHub}>Sign in with GitHub</button>
    </div>
  );
}

export default AuthScreen;
