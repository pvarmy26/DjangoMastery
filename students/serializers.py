from rest_framework import serializers
from .models import Student


def validate_marks_range(value):
    if value < 0 or value > 100:
        raise serializers.ValidationError(
            "Marks must be between 0 and 100."
        )


class StudentSerializer(serializers.ModelSerializer):

    marks = serializers.IntegerField(
        validators=[validate_marks_range]
    )

    def validate_age(self, value):
        if value < 16:
            raise serializers.ValidationError(
                "Student age must be at least 16."
            )
        return value

    def validate(self, data):
        age = data.get("age")
        course = data.get("course")

        if course == "Advanced Python" and age < 18:
            raise serializers.ValidationError(
                "Advanced Python requires age 18 or above."
            )

        return data

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ["id", "created_at"]