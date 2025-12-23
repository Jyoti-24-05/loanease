const ResultCard = ({ data }) => {
  if (!data) return null;

  return (
    <div className="result-card">
      <h3>✅ Loan Result</h3>
      <p><strong>KYC Status:</strong> {data.kyc_status}</p>
      <p><strong>Credit Score:</strong> {data.credit_score}</p>
      <p><strong>Decision:</strong> {data.decision}</p>

      {data.sanction_letter && (
        <a
          href={`http://127.0.0.1:8000/${data.sanction_letter}`}
          target="_blank"
          rel="noreferrer"
        >
          📄 Download Sanction Letter
        </a>
      )}
    </div>
  );
};

export default ResultCard;
