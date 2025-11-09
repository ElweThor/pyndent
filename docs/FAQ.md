# Frequently Asked Questions

- Q: [Why should I agree to inflate by a 20% average my Python code?](#plus20pct)
- Q: [But 20% is a lot of overhead!](#overhead)
- Q: [Can I use Pyndent in CI/CD pipelines?](#CICD_validate)
- Q: [What about existing Python code?](#restore)
- Q: [GUI support?](#PynGUI)
- Q: [Why this tool is open source and with so permissive license?](#whyopensource)

- _**note**_: always check the [ROADMAP](docs/ROADMAP.md), to see if a feature is available already.

<a name="plus20pct"></a>
## Q: Why should I agree to inflate by a 20% average my Python code?

`A`: That's the _wrong question_: the **real** one is: _do you agree to have 'randomic execution', in a large program made by thousand of code lines, just 'cause a tab is missing **and** with Python agreeing to execute your code?_  
In other terms: _do you like to lose hours (or days), debugging ALL the program's logic again, only 'cause a single line moved 4 characters to the left?_  

If you answered **YES** to both of the above questions, you don't need Pyndent at all.  
(_but, maybe, your boss would like to know how you pass your days_ 😉)

<a name="overhead"></a>
## Q: But 20% is a lot of overhead!

`A`: Consider this:  
- 20% (average) file size increase ✅  
- 100% (sure) confidence in block structure ✅  
- 0% risk of silent logic errors ✅  
- Team collaboration without indent wars ✅  

The math is clear! 🧮

<a name="CICD_validate"></a>
## Q: Can I use Pyndent in CI/CD pipelines?

`A`: Absolutely! Pyndent is perfect for CI/CD environments. You can:

- Validate structure before deployment:

```yaml
- name: Check Pyndent delimiters
  run: pyndent --validate *.pyn
```

- Pre-commit hooks to prevent unbalanced blocks:

```yaml
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: pyndent-check
      name: Pyndent structure validation
      entry: pyndent --validate
      language: system
      files: '\.pyn$'
```

- Build step for processing before testing:

```yaml
- name: Build Python from Pyndent
  run: pyndent src/ -o build/ -s
- name: Run tests
  run: python -m pytest build/
```

Pyndent ensures your **block structure** is always correct before code reaches production, catching indentation-related bugs that Python would silently execute!

<a name="restore"></a>
## Q: What about existing Python code?

`A`: **-r/--restore** will work for you (if the existing Python code <ins>is executable already</ins>).

<a name="PynGUI"></a>
## Q: GUI support?

`A`: **PynGUI** is going to be developed: look at the [ROADMAP](docs/ROADMAP.md).

<a name="whyopensource"></a>
## Q: Why this tool is open source and with so permissive license?

`A`: As a matter of fact, the answers are many:  
- I already have a nice job, which gives me headaches, sometimes, but usually a lot of fun, and it's interesting too!  
- My job already pays me enough: I don't need to enter "_Forbes' Billionaires List_", nor the "_Fortune Global 500_", which could give me far **more** (and not-that-fun) headaches.  
- I love to share.  
- I written Pyndent **for me**, mostly... but why not giving Python's community something to play with?  
