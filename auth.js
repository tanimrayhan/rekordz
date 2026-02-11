import { auth } from "./firebase.js";
import {
  GoogleAuthProvider,
  signInWithPopup,
  signOut,
  onAuthStateChanged
} from "https://www.gstatic.com/firebasejs/12.9.0/firebase-auth.js";

const provider = new GoogleAuthProvider();

/* =========================
   LOGIN (Google)
========================= */
window.login = async () => {
  try {
    await signInWithPopup(auth, provider);
    // redirect is handled by onAuthStateChanged
  } catch (err) {
    console.error("Login failed:", err);
    alert("Login failed. Try again.");
  }
};

/* signup = login (same for Google) */
window.signup = window.login;

/* =========================
   LOGOUT
========================= */
window.logout = async () => {
  await sig
