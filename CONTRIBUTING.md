# Contributing to Meshtastic Basic Bot

Thank you for your interest in contributing! This project is a starting point for Meshtastic bot development, and contributions are welcome.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, Meshtastic hardware)
- Relevant log files from `logs/` directory

### Suggesting Features

Have an idea for a new feature? Open an issue with:
- Clear description of the feature
- Use case / why it would be useful
- Example of how it would work
- Any implementation ideas (optional)

### Pull Requests

1. **Fork the repository**

2. **Create a feature branch**:
   ```bash
   git checkout -b feature/my-new-feature
   ```

3. **Make your changes**:
   - Keep code simple and readable
   - Follow existing code style
   - Add comments for complex logic
   - Update README if needed

4. **Test your changes**:
   - Test on your own Meshtastic hardware
   - Ensure bot starts and connects properly
   - Verify new features work as expected

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/my-new-feature
   ```

7. **Open a Pull Request**:
   - Describe what the PR does
   - Reference any related issues
   - Include screenshots/examples if applicable

## Code Style

- **Python**: Follow PEP 8 style guide
- **Comments**: Use clear, concise comments
- **Naming**: Use descriptive variable and function names
- **Simplicity**: Keep the codebase simple for beginners

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/meshtastic-basic-bot.git
   cd meshtastic-basic-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make your changes and test locally

4. Submit PR when ready

## Feature Ideas

Looking for something to work on? Here are some ideas:

### Version 1.1 - Command Support
- Parse incoming messages for commands (e.g., "!help", "!ping")
- Multiple response types based on command
- Help command to list available features

### Version 1.2 - Enhanced Responses
- Conditional responses (different replies for different keywords)
- Time-based responses (different replies at different times)
- User-specific responses (remember previous conversations)

### Version 1.3 - External Integration
- Weather API integration
- News headlines
- Jokes/quotes database
- Calculator/utility functions

### Version 1.4 - Advanced Features
- Message scheduling
- Statistics tracking
- Multi-node support
- Configuration file support

## Questions?

Feel free to:
- Open an issue for questions
- Join the [Meshtastic Discord](https://discord.gg/meshtastic)
- Check the [Meshtastic documentation](https://meshtastic.org/docs/)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
