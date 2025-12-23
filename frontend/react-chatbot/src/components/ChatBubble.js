const ChatBubble = ({ message, sender }) => {
  return (
    <div className={`bubble ${sender}`}>
      {message}
    </div>
  );
};

export default ChatBubble;
