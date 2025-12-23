import { useState } from "react";
import { applyLoan } from "../services/api";
import ChatBubble from "./ChatBubble";
import Loader from "./Loader";
import ResultCard from "./ResultCard";

const Chatbot = () => {
  const [messages, setMessages] = useState([
    { text: "Hi! I can help you apply for a loan 💼", sender: "bot" }
  ]);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleApply = async () => {
    setLoading(true);

    const payload = {
      name: "Jyoti",
      phone: "9999999999",
      email: "jyoti@test.com",
      address: "Ranchi",
      loan_amount: 200000,
      tenure_months: 24
    };

    try {
      const res = await applyLoan(payload);
      setResult(res.data.data);

      setMessages(prev => [
        ...prev,
        { text: "Loan processed successfully 🎉", sender: "bot" }
      ]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { text: "❌ Something went wrong. Try again.", sender: "bot" }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <h2>LoanEase Chatbot</h2>

      <div className="chat-box">
        {messages.map((m, i) => (
          <ChatBubble key={i} message={m.text} sender={m.sender} />
        ))}
        {loading && <Loader />}
      </div>

      <button onClick={handleApply}>
        Apply for Loan
      </button>

      <ResultCard data={result} />
    </div>
  );
};

export default Chatbot;
