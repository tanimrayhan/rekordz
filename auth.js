import { auth } from "./firebase.js";
import {
  GoogleAuthProvider,
  signInWithPopup,
  signOut,
  onAuthStateChanged
} from "https://www.gstatic.com/firebasejs/12.9.0/firebase-auth.js";

const provider = new GoogleAuthProvider();

/* LOGIN / SIGNUP */
window.login = async () => {
  await signInWithPopup(auth, provider);
};

window.signup = window.login;

/* LOGOUT */
window.logout = async () => {
  await signOut(auth);
};

/* AUTH GUARD */
onAuthStateChanged(auth, user => {
  if (!user && !location.pathname.endsWith("index.html")) {
    location.href = "index.html";
  }
});
