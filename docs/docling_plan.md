# Docling Integration Plan

RefLens AI uses football rule context to explain referee and VAR decisions.

## Purpose of Docling

Docling will be used to convert football rule documents from PDF or web formats into structured text that can be searched by the app.

## Planned Flow

```text
Football Rule PDF
   |
   v
Docling Document Conversion
   |
   v
Structured Markdown/Text
   |
   v
Rule Retriever
   |
   v
Relevant Rule Context
   |
   v
IBM Granite Explanation
```

## MVP Status

The current MVP uses a small local rule dictionary in `src/rule_retriever.py`.

Future versions will replace or expand this dictionary with Docling-processed football rule documents.
