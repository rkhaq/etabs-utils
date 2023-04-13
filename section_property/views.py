from rest_framework.views import APIView
from rest_framework.response import Response
import json
import re

class VerifySectionsView(APIView):
    def post(self, request):
        sections = request.data.get("sections")

        if not sections:
            return Response({"error": "No sections provided."}, status=400)

        misnamed_sections = []
        pattern = re.compile(r'^C(\d+)x(\d+)C(\d+)$')

        for section_name, section_data in sections.items():
            match = pattern.match(section_name)

            if not match:
                misnamed_sections.append((section_name, section_data))
                continue

            depth, width, fc = map(int, match.groups())

            if (section_data["depth"] != depth or
                section_data["width"] != width or
                section_data["fc"] != fc):
                misnamed_sections.append((section_name, section_data))

        return Response({"misnamed_sections": misnamed_sections})