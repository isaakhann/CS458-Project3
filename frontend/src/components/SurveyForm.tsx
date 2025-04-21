import { useState } from 'react';

const aiModels = ['ChatGPT', 'Bard', 'Claude', 'Copilot', 'Other'];

function SurveyForm() {
  const [selectedModels, setSelectedModels] = useState<string[]>([]);
  const [modelCons, setModelCons] = useState<{ [model: string]: string }>({});

  const toggleModel = (model: string) => {
    setSelectedModels((prev) =>
      prev.includes(model) ? prev.filter((m) => m !== model) : [...prev, model]
    );
  };

  const handleConChange = (model: string, value: string) => {
    setModelCons((prev) => ({ ...prev, [model]: value }));
  };

  return (
    <form>
      <div className="form-question">
        <label>Name–Surname</label>
        <input type="text" placeholder="Enter your full name" />
      </div>

      <div className="form-question">
        <label>Birth Date</label>
        <input type="date" />
      </div>

      <div className="form-question">
        <label>Education Level</label>
        <select>
          <option value="">Select Education Level</option>
          <option>High School</option>
          <option>Bachelor's</option>
          <option>Master's</option>
          <option>PhD</option>
          <option>Other</option>
        </select>
      </div>

      <div className="form-question">
        <label>City</label>
        <input type="text" placeholder="Enter your city" />
      </div>

      <div className="form-question">
        <label>Gender</label>
        <label>
          <input type="radio" name="gender" value="male" /> Male
        </label>
        <label>
          <input type="radio" name="gender" value="female" /> Female
        </label>
      </div>

      <div className="form-question">
        <label>AI Models You've Tried</label>
        {aiModels.map((model) => (
          <div key={model}>
            <label>
              <input
                type="checkbox"
                value={model}
                checked={selectedModels.includes(model)}
                onChange={() => toggleModel(model)}
              />{' '}
              {model}
            </label>

            {selectedModels.includes(model) && (
              <input
                type="text"
                placeholder={`Pros and cons of ${model} (optional)`}
                value={modelCons[model] || ''}
                onChange={(e) => handleConChange(model, e.target.value)}
                style={{ marginTop: '8px' }}
              />
            )}
          </div>
        ))}
      </div>

      <div className="form-question">
        <label>Beneficial Use Cases of AI in Daily Life</label>
        <textarea placeholder="Describe any AI use cases that benefit your daily life..." />
      </div>

      <button type="submit">Submit</button>
    </form>
  );
}

export default SurveyForm;
