import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: 'AIzaSyCgZ9ta6Mp5jH3ZzqrZ7IV7kD81zRdzKIE',
  authDomain: 'project1-cs458.firebaseapp.com',
  projectId: 'project1-cs458',
  storageBucket: 'project1-cs458.firebasestorage.app',
  messagingSenderId: '100695855863',
  appId: '1:100695855863:web:14bb57f066794abdecb9f2',
  measurementId: 'G-M23V1SV2NQ',
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);

export default app;
